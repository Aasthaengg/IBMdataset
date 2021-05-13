n=int(input());d,s=input(),input()
for i in range(n,2*n):
    kaburi=2*n-i
    if d[-kaburi:]==s[:kaburi]:print(i);exit()
print(2*n)