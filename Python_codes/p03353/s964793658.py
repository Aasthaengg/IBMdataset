def main():
    s = input()
    k = int(input())
    lst = set()
    l = len(s)
    for i in range(l):
        for j in range(i, i + k):
            lst.add(s[i:j+1])
    lst = list(lst)
    lst.sort()
    print(lst[k - 1])
main()