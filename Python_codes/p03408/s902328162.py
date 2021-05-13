# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline

    word_dict = {}
    n = int(input().rstrip())
    for i in range(n):
        s = input().rstrip()
        if s not in word_dict:
            word_dict[s] = 0
        word_dict[s] += 1

    m = int(input().rstrip())
    for i in range(m):
        s = input().rstrip()
        if s not in word_dict:
            word_dict[s] = 0
        word_dict[s] -= 1

    ans = max(word_dict.values())
    print(ans if ans > 0 else 0)

if __name__ == "__main__":
    resolve()
