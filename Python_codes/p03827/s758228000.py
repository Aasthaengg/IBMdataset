n = int(input())
s = str(input())

x = [0] * 101
for i in range(n):
    if(s[i]=='I'):
        x[i+1] = x[i] + 1
    else:
        x[i+1] = x[i] - 1
    
print(max(x))