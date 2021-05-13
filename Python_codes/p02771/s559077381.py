def main():
    s = list(map(int,input().strip().split()))

    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")
    return
main()
