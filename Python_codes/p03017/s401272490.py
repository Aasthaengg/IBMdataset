n,a,b,c,d = map(int,input().split())
s = input()
if "##" in s[min(a,b)-1:max(c,d)]:
    print("No")
else:
    if d > c:
        print("Yes")
    else:
        for i in range(b-1,d):
            if s[i-1] == "." and s[i] == "." and s[i+1] == ".":
                print("Yes")
                break
        else:
            print("No")