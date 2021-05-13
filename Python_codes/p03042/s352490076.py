def main():
    inp=input()
    ch1=int(inp[0:2])
    ch2=int(inp[2:])
    if inp[0]==0:
        ch1=int(inp[1])
    if inp[2]==0:
        ch2=int(inp[-1])
    if ch1<=12 and ch1>=1:
        if ch2<=12 and ch2>=1 and ch2<=12 and ch2>=1:
            print("AMBIGUOUS")
            return
        elif ch2<=12 or ch2>=1:
            print("MMYY")
            return
    if ch1>12 or ch1<1:
        if ch2<=12 and ch2>=1:
            print("YYMM")
            return
        else:
            print("NA")
            return
main()