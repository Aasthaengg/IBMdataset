# C - Digits in Multiplication
def main():
    n = int(input())
    ans = []

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(max(len(str(i)), len(str(n//i))))
    else:
        print(min(ans))



        
if __name__ == '__main__':
    main()