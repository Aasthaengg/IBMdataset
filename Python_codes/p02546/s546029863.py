def main():
    import sys
    inl = sys.stdin.buffer.readline
    
    n = input()

    if(n[len(n)-1] =="s"):
        n+='es'
    else:
        n+='s'
    print(n)


        


    




















if __name__ == "__main__":
    main()