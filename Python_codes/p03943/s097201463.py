def main():
    a, b, c = map(int, input().split())

    flag = False

    if a == b + c :
        flag = True
    if b == a + c :
        flag = True
    if c == b + a :
        flag = True

    if flag == True:
        print("Yes")
    else:
        print("No")
main()