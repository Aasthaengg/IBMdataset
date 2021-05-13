def main():
    N = input()
    c = [c for c in N]
    if((c[0] == c[1] and c[0] == c[2]) or (c[1] == c[2] and c[1] == c[3])):
        print("Yes")
    else:
        print("No")

main()