# AOJ ITP1_9_D

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    string = input()
    n = int(input())
    for i in range(n):
        command = input().split()
        a = int(command[1])
        b = int(command[2])
        if command[0][0] == 'r':
            front = string[0 : a]
            back = string[b + 1 : len(string)]
        if command[0][2] == 'p':
            string = front + command[3] + back
        elif command[0][2] == 'v':
            string = front + string[a : b + 1][::-1] + back
        else:
            print(string[a : b + 1])

if __name__ == "__main__":
    main()
