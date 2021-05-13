import copy
def main():
    n, a, b, c, d = map(int, input().split())
    step = list(input())

    sn = a - 1
    fn = b - 1

    sn_goal = False
    fn_goal = False
    jump = -1
    
    while True:
        if d < c:
            if (step[fn - 1] == ".") and (step[fn + 1] == "."):
                jump = copy.deepcopy(fn)

        if fn == d - 1:
            fn_goal = True
            break

        if step[fn + 1] == ".":
            fn += 1
        elif step[fn + 2] == ".":
            fn += 2
        else:
            break

    if d < c:
        if jump == -1:
            print("No")
            exit()

        step[jump] = "#"

    while True:
        if sn == c - 1:
            sn_goal = True
            break

        if step[sn + 1] == ".":
            sn += 1
        elif step[sn + 2] == ".":
            sn += 2
        else:
            break
    
    if sn_goal and fn_goal:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()