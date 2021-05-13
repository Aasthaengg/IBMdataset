import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    e_value = [(1 + i)/2 for i in p]
    c_value = [e_value[0]]
    for i in range(1, n):
        c_value.append(c_value[i-1] + e_value[i])
    ans = 0
    for i in range(k-1, n):
        if i == k-1:
            ans = c_value[i]
        else:
            ans = max(ans, c_value[i]-c_value[i-k])
    print(ans)
    
if __name__ == '__main__':
    main()