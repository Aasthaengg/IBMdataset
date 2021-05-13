

def main():
    
    input_lines_n = input()
    n = int(input_lines_n)
    
    input_lines_a = input()
    arrA = input_lines_a.split(" ")
    
    cnt = 0
    for i in range(0, len(arrA)):
        if i % 2 == 0:
            if int(arrA[i]) % 2 != 0:
#                print(arrA[i])
                cnt = cnt + 1
    
    print(cnt)
    
if __name__ == "__main__":
    main()
