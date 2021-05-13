S = input()

def solve(T) :
    while 1:
        for i in ("dream", "dreamer", "erase", "eraser"):
            if T.endswith(i):
                T = T[: -len(i)]
                break
        
        else:
            print("NO")
            break
        
        if not T:
            print("YES")
            break

solve(S)