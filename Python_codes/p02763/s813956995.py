class segtree:

    def __init__(self, n, identity):
        # identityは初期値
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_end_leaves = 2 ** (len(nb) - 1)
        else:
            self.num_end_leaves = 2 ** (len(nb))

        self.array = [identity for i in range(self.num_end_leaves * 2)]
        self.identity = identity

    def update(self, x, val):
        actual_x = x + self.num_end_leaves
        self.array[actual_x] = val
        while actual_x > 0:
            actual_x = actual_x // 2
            self.array[actual_x] = self.array[actual_x * 2] | self.array[actual_x * 2 + 1]

    def get(self, q_left, q_right, arr_ind=1, leaf_left=0, depth=0):
        width_of_floor = self.num_end_leaves // (2 ** depth)
        leaf_right = leaf_left + width_of_floor - 1

        if leaf_left > q_right or leaf_right < q_left:
            return self.identity

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]

        else:
            val_l = self.get(q_left, q_right, 2 * arr_ind, leaf_left, depth + 1)
            val_r = self.get(q_left, q_right, 2 * arr_ind + 1, leaf_left + width_of_floor // 2, depth + 1)
            return val_l | val_r

N = int(input())
S = list(input())
Q = int(input())
T = {}
j = 1
for i in range(97, 97+26):
    T[chr(i)] = j
    j *= 2

s_tree = segtree(N+1, 0)

for i in range(N):
    s_tree.update(i+1, T[S[i]])

for i in range(Q):
    A = list(input().split())
    a, b, c = A
    if a == "2":
        K = bin(s_tree.get(int(b), int(c)))[2:]
        d = 0
        for i in K:
            if i == "1":
                d += 1
        print(d)
    else:
        s_tree.update(int(b), T[c])