# A - Grouping
def main():
    x, y = map(int, input().split())
    g_a = [1, 3 , 5, 7, 8, 10, 12]
    g_b = [4, 6, 9, 11]
    g_c = [2]

    if x in g_a and y in g_a:
        print('Yes')
    elif x in g_b and y in g_b:
        print('Yes')
    elif x in g_c and y in g_c:
        print('Yes')
    else:
        print('No')

if __name__ ==  "__main__":
    main()