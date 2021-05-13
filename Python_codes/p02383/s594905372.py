class Dice:
    """Dice class"""

    def __init__(self):                  # ?????????????????????
        self.eyeIndex = 1        #center
        self.eyeIndex_E = 3      #east
        self.eyeIndex_W = 4      #west
        self.eyeIndex_N = 5      #north
        self.eyeIndex_S = 2      #south
        self.eye = 0
        
    def shakeDice(self, in_command):

        pre_eyeIndex = self.eyeIndex
        if in_command == "E":
            self.eyeIndex = self.eyeIndex_W 
            self.eyeIndex_E = pre_eyeIndex 
            self.eyeIndex_W = 7 - self.eyeIndex_E
            
        elif in_command == "W":
            self.eyeIndex = self.eyeIndex_E 
            self.eyeIndex_W = pre_eyeIndex
            self.eyeIndex_E = 7 - self.eyeIndex_W
            
        elif in_command == "N":
            self.eyeIndex = self.eyeIndex_S 
            self.eyeIndex_N = pre_eyeIndex 
            self.eyeIndex_S = 7 - self.eyeIndex_N

        elif in_command == "S":
            self.eyeIndex = self.eyeIndex_N         
            self.eyeIndex_S = pre_eyeIndex 
            self.eyeIndex_N = 7 - self.eyeIndex_S 
            
        self.eye = self.eyes[self.eyeIndex]

    def getEye(self):
        return self.eye

    def setEyes(self, eyes):             # setEyes()???????????? ???????????????
        
        #index???1???????????????????????§,??????????????????????????????
        eyes = "0 " + eyes
        self.eyes = list(map(int, eyes.split(" ")))


dice_1 = Dice()
dice_1.setEyes(input().rstrip())

input_commands = input().rstrip()

for i in range(len(input_commands)):
    #Shake dice!!
    dice_1.shakeDice(input_commands[i])

print(dice_1.getEye())