def resolve():
    l1, l2, r1, r2 = map(int, input().split())
    lw = l1 + l2
    rw = r1 + r2
    
    ans = ""
    if lw < rw:
        ans = "Right"
    elif lw > rw:
        ans = "Left"
    else:
        ans = "Balanced"
    print(ans)
resolve()