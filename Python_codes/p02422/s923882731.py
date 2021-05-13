target = raw_input()

command = []
for _ in range(int(raw_input())):
    command += [raw_input()]

for c in command:
    cmd = c.split()
    if 'replace' == cmd[0]:
        #print   target[0:int(cmd[1])] + cmd[3] + target[int(cmd[2])+1:len(target)]
        target = target[0:int(cmd[1])] + cmd[3] + target[int(cmd[2])+1:len(target)]
    if 'reverse' == cmd[0]:
        #print target[int(cmd[1]):int(cmd[2])+1]
        target = target[0:int(cmd[1])] + target[int(cmd[1]):int(cmd[2])+1][::-1] + target[int(cmd[2])+1:len(target)]
    if 'print' == cmd[0]:
       print target[int(cmd[1]):int(cmd[2])+1]