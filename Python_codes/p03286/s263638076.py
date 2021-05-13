n = int(input())
ans = []
for i in range(100):
    if n%(2**(i+1))>0:
        ans.append('1')
        n -= (-2)**i
    else:
        ans.append('0')
    if n==0:
        break
print(''.join(ans[::-1]))