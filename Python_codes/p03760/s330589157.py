# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    o = input().rstrip()
    e = input().rstrip()

    ans = ""
    for i in range(len(o)):
        ans += o[i]
        if i < len(e):
            ans += e[i]

    print(ans)

if __name__ == "__main__":
    resolve()
