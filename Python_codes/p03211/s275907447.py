s=input();m=float('inf')
for i in range(len(s)-2): m=min(m,abs(int(s[i:i+3])-753))
print(m)