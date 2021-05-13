n = int(input())
s = input()
if n%2 == 0:
    cnt = 0
    for i in range(n//2):
        if s[i] == s[i + n//2]:
            cnt += 1
            if cnt == n//2:
                print("Yes")
                break
        else:
            print("No")  
            break
else:
    print("No")