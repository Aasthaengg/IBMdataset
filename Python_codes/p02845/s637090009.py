import sys
n = int(input())
a_ls = list(map(int, input().split()))
hat_nperson = [0,0,1]
ans = 3
mod = 10**9+7

if a_ls[0] != 0 or (n != 1 and a_ls[1] == 2):
    print(0)
    sys.exit()

for i in range(1,n):
    n_same = a_ls[i]
    n_choices = 0
    choice_ind = -1
    for j,person in enumerate(hat_nperson):
        if person == n_same:
            n_choices += 1
            choice_ind = j
    if choice_ind == -1:
        print(0)
        sys.exit()
    hat_nperson[choice_ind] += 1
    ans *= n_choices
    ans %= mod
print(ans%mod)