def main():
    R = int(input())
    if(R<1200):
        result = 'ABC'
    elif(R<2800):
        result = 'ARC'
    else:
        result = 'AGC'
    print(result)

if __name__ == "__main__":
    main()