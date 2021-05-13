# coding: utf-8
# Your code here!
def num2alpha(x):
    if x <= 26:
        return chr(x + 64).lower()
    elif x % 26 == 0:
        return num2alpha(x // 26 -1) + chr(90).lower()
    else:
        return num2alpha(x // 26) + chr(x % 26 + 64).lower()  

def main():
    n = int(input())
    print(num2alpha(n))
    
main()