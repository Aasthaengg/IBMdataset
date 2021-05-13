def main():
    s = input()
    cubes = []
    for c in s:
        if c == "0":
            cubes.append("red")
        else:
            cubes.append("blue")

    buffer = [] #キューブの一時保存場所。同じ色が続くとここにたまっていく
    buffer.append(cubes.pop()) #cubesの最後の要素をbufferの最後に移し替える。
    counter = 0
    while cubes:
        if len(buffer) <= 0 or buffer[-1] == cubes[-1]: #bufferが空じゃないことを確認してからbufferとcubesの最後の要素を比較
            buffer.append(cubes.pop()) #同じ色はbufferに格納
        else: #もし違う色だったら
            buffer.pop() #bufferの最後のキューブをひとつ消す
            cubes.pop() #cubesの最後のキューブをひとつ消す
            counter += 2 #2個消去
    print(counter)




if __name__ == '__main__':
    main()
