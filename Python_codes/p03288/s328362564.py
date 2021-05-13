n=int(input())
if(n<=1199):
    print("ABC")
else:
    print("ARC" if n<=2799 else "AGC")