N = input()
l = len(N)
ans = 0

if l == 1:
    ans = int(N)
elif l == 2:
    ans = 9
elif l == 3:
    ans =  int(N) + 9 - 99
elif l == 4:
    ans = 909
elif l == 5:
    ans = int(N)+ 909 - 9999
else:
    ans = 90909
    
print(ans)