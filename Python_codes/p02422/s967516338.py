#-*-coding:utf-8-*-

def main():
    s = input()
    n = int(input())
    for _ in range(n):
        commands=input().split()
        if commands[0]=="replace":
            s=s[:int(commands[1])]+commands[3]+s[int(commands[2])+1:]
        elif commands[0]=="reverse":
            reverse_point=s[int(commands[1]):int(commands[2])+1]
            s=s[:int(commands[1])]+reverse_point[::-1]+s[int(commands[2])+1:]
        elif commands[0]=="print":
            print(s[int(commands[1]):int(commands[2])+1])

if __name__=="__main__":
    main()
