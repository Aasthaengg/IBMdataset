
def main():
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    sum_a = sum(a)
    cnt = 0
    for i in a:
        if i * 4* m >= sum_a:
            cnt+=1
    if cnt>= m:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()