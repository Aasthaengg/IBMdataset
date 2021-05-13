#%%
a = list(input())
c = [0] * 26
alpha2num = lambda x: ord(x) - ord('a') 

for i in range(len(a)):
    c[alpha2num(a[i])] += 1

ans = 1 + (len(a)*(len(a)-1)//2)
for i in range(26):
    ans -= c[i] * (c[i] - 1) //2

print(ans)

#%%
