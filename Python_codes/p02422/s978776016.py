# -*-coding:utf-8

def main():

    inputLine = list(input())

    orderLine = int(input())

    for i in range(orderLine):
        tokens = list(input().split())

        a = int(tokens[1])
        b = int(tokens[2])

        if(tokens[0] == 'print'):
            print( ''.join(inputLine[a:b+1]) )
        elif(tokens[0] == 'reverse'):
            reverseList = inputLine[a:b+1]
            inputLine[a:b+1] = reverseList[::-1]
        elif(tokens[0] == 'replace'):
            replaceList = list(tokens[3])
            inputLine[a:b+1] = replaceList

if __name__ == '__main__':
    main()