n,a,b,c,d = map(int,input().split())
s = [i == "#" for i in list(input())]
s.append(False)
def check_route(x,y):
    for i in range(x,y):
        if s[i] and s[i+1]:
            return False
    return True

def check_three(x,y):
    for i in range(x-1,y):
        if (not s[i]) and (not s[i+1]) and (not s[i+2]):
            return True
    return False

if c < d:
    if check_route(a-1,c-1) and check_route(b-1,d-1):
        print("Yes")
    else:
        print("No")
else:
    if check_route(a-1,c-1) and check_route(b-1,d-1):
        if check_three(b-1,d-1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")