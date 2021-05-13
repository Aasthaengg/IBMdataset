
def resolve():
    X, Y, A, B, C = map(int, input().split())
    apple_A = sorted(map(int, input().split()), reverse=True)[:X]
    apple_B = sorted(map(int, input().split()), reverse=True)[:Y]
    apple_C = sorted(map(int, input().split()), reverse=True)

    ans = apple_A + apple_B + apple_C
    ans.sort(reverse=True)
    
    print(sum(ans[:X+Y]))

if __name__ == "__main__":
    resolve()
