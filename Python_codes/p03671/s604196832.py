def main():
    a, b, c = map(int, input().split())
    p_list = sorted([a, b, c])
    print(p_list[0] + p_list[1])
main()