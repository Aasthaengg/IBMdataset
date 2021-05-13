# coding: utf-8

def main():
    x = int(input())
    
    money = 100
    i = 0
    while money < x:
        money = money * 101 // 100
        i += 1
    
    print(i)
    
main()