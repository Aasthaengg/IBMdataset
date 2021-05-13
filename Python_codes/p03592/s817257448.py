import sys

def main():
    n, m, k = map(int, input().split())
    cnt = set()
    for x in range(n+1):
        for y in range(m+1):
            tmp = x*y + (n-x)*(m-y)
            if tmp not in cnt:
                cnt.add(tmp)

    if k in cnt:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()