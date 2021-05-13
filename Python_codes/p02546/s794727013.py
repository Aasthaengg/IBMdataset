def main():
    n = list(str(input()))
    if n[-1] == "s":
        n.append("es")
    else :
        n.append("s")
    print(''.join(n))
main()