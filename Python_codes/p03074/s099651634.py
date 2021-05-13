from itertools import accumulate

def main():
    n, k = map(int, input().split())
    s = input()
    z = [len(i) for i in s.split("1") if i]
    o = [0] * (s[0] == "0") + [len(i) for i in s.split("0") if i] + [0]
    az = [0] + list(accumulate(z))
    ao = [0] + list(accumulate(o))
    if k < len(z):
        print(max(ao[i + k + 1] - ao[i] + az[i + k] - az[i] for i in range(len(z) - k + 1)))
    else:
        print(n)

if __name__ == '__main__':
    main()