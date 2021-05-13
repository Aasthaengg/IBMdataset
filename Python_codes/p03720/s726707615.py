
url = "https://atcoder.jp//contests/abc061/tasks/abc061_b"

def main():
    t = list(map(int, input().split()))
    rode = [0] * t[0]
    for i in range(t[1]):
        r = list(map(int, input().split()))
        rode[r[0]-1] += 1
        rode[r[1]-1] += 1
    for v in rode:
        print(v)



if __name__ == '__main__':
    main()
