def resolve():
    n = input()
    ans = ""

    for i in range(len(n)-2):
        if n[i] == n[i+1] and n[i] == n[i+2]:
            ans = "Yes"
            break
        else:
            ans = "No"
    print(ans)
resolve()