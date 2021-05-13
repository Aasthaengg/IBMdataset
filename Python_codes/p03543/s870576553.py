N=int(input())
print("No" if N//10%111 and N%1000%111 else "Yes")