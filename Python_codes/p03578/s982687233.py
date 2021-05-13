from collections import Counter
def main():
    N, D = int(input()), Counter(list(map(int, input().split())))
    M, T = int(input()), Counter(list(map(int, input().split())))
    result = "YES"
    for key, value in T.items():
        temp = D.get(key)
        if temp == None or temp < value:
            result = "NO"
            break
    print(result)
main()