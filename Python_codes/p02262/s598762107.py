n = int(input())
arr = [int(input()) for index in range(n)]

cnt, m = 0, 0
G = []


def insertion_sort(nums, n, g):
    global cnt
    for idx1 in range(g, n):
        v = nums[idx1]
        idx2 = idx1 - g
        while idx2 >= 0 and nums[idx2] > v:
            nums[idx2+g] = nums[idx2]
            idx2 -= g
            cnt  += 1
        nums[idx2+g] = v

h = 1
while not h > n:
    G.append(h)
    h = 3 * h + 1

m = len(G)
G.reverse()

for index in range(m):
    insertion_sort(arr, n, G[index])


print(m)
print(" ".join(map(str, G)))
print(cnt)
for i in range(n):
	print(arr[i])
