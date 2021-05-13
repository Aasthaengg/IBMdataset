a,b,c,d,e,f = map(int, input().split())
s_max = f*e//(e+100)
w_max = f//100

s=[]
w=[]

max = 0
ans = [100*a,0]
for i in range(s_max//c+1):
    for j in range(s_max//d+1):
        if c*i + d*j <= s_max:
            s.append(c*i + d*j)

for i in range(w_max//a+1):
    for j in range(w_max//b+1):
        if 0<a*i + b*j <= w_max:
            w.append(a*i + b*j)

for i in range(len(s)):
    for j in range(len(w)):
        if s[i]/(w[j]*100+s[i])<=e/(e+100) and s[i]/(w[j]*100+s[i])>=max and w[j]*100+s[i]<=f:
            max = s[i]/(w[j]*100+s[i])
            ans = [w[j]*100+s[i],s[i]]

print(ans[0],ans[1])
