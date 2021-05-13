if __name__ == "__main__":
    n = int(input())
    s_dict = {}
    for i in range(n):
        commandLine = input().split()
        if commandLine[0] == "insert":
            s_dict[commandLine[1]] = commandLine[1]
        elif commandLine[0] == "find":
            if s_dict.get(commandLine[1]) != None:
                print("yes")
            else:
                print("no")

