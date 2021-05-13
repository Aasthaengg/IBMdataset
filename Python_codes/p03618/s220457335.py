A = input()
n = len(A)
alpha_dic = {}

for a in A:
    alpha_dic[a] = 1 + alpha_dic.get(a, 0)

ans = n * (n-1) //2
for key, num in alpha_dic.items():
    ans -= (num * (num-1) // 2)
print(ans+1)
