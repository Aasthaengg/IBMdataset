
S = str(input())


if __name__ == "__main__":
    def func():
        h_pointer = False
        i_pointer = False
        check = True

        if(len(S)%2 != 0):
            print('No') 
            return

        for i in range(0, len(S) ):
            if(h_pointer and i_pointer == False and S[i] == "i"):
                h_pointer = False

            elif(h_pointer == False and i_pointer == False and S[i] == "h"):
                h_pointer = True
            else:
                print('No')
                check = False
                break
            
            # print(h_pointer, i_pointer, check)


        if check: 
            print('Yes')
    
    func()

