n = int(input())
s = input()

if n % 2 != 0 :
    print("No")
else :
    t = ""
    for i in range(n//2):
        t += s[i]
    if s != t+t :
        print("No")
    else :
        print("Yes")
