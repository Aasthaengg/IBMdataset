def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
        return
    else:
        r = ""
        for rr in range(k):
            r += s[rr]
        r += "..."
        print(r)
        return 

main()