def main():
    a, b, k = map(int, input().split(" "))
    temp = min(a, k)
    a -= temp
    k -= temp
    b -= min(b, k)
    print(a, b)
main()